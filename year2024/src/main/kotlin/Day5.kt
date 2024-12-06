class Day5 : Day(5) {
  override fun getPart1(): Any =
    getLinePartition().let { linePartition ->
      getCorrectUpdates(
        getRules(linePartition), getUpdates(linePartition)
      )
    }.let(::sumOfMiddlePageNumbers)

  private fun getLinePartition(): Pair<List<String>, List<String>> {
    val lines = getLines(getFilename(1))
      .filter { it.isNotBlank() }
      .partition { it.contains("|") }
    return lines
  }

  private fun getRules(partition: Pair<List<String>, List<String>>): List<Pair<Int, Int>> =
    partition.first
      .map { it.split("|").map(String::toInt) }
      .map { it[0] to it[1] }

  private fun getUpdates(partition: Pair<List<String>, List<String>>): List<List<Int>> =
    partition.second.map { it.split(",").map(String::toInt) }

  private fun getCorrectUpdates(rules: List<Pair<Int, Int>>, updates: List<List<Int>>): List<List<Int>> =
    updates.filter { isUpdateCorrect(it, rules) }

  private fun isUpdateCorrect(pages: List<Int>, rules: List<Pair<Int, Int>>): Boolean =
    pages.all { page -> isPageCorrect(rules, page, pages) }

  private fun isPageCorrect(
    rules: List<Pair<Int, Int>>,
    page: Int,
    pages: List<Int>
  ): Boolean =
    rules.filter { rule -> isRuleForPage(page, rule) }
      .filter { rule -> isRuleInPages(pages, rule) }
      .all { rule -> isPageCorrectForRule(pages, rule) }

  private fun isRuleInPages(pages: List<Int>, it: Pair<Int, Int>) = it.second in pages

  private fun isRuleForPage(page: Int, rule: Pair<Int, Int>) = page == rule.first

  private fun isPageCorrectForRule(pages: List<Int>, rule: Pair<Int, Int>) =
    pages.indexOf(rule.first) < pages.indexOf(rule.second)

  private fun sumOfMiddlePageNumbers(updates: List<List<Int>>): Int =
    updates.sumOf { it[it.size / 2] }

  override fun getPart2(): Any =
    getLinePartition().let { linePartition ->
      val rules = getRules(linePartition)
      getInCorrectUpdates(
        rules, getUpdates(linePartition)
      )
        .map { pages -> getOrderedUpdate(pages, rules) }
    }.let(::sumOfMiddlePageNumbers)

  private fun getInCorrectUpdates(rules: List<Pair<Int, Int>>, updates: List<List<Int>>): List<List<Int>> =
    updates.filterNot { isUpdateCorrect(it, rules) }

  private fun getOrderedUpdate(pages: List<Int>, rules: List<Pair<Int, Int>>): List<Int> {
    val ordered = pages.toMutableList()
    while (!isUpdateCorrect(ordered, rules)) {
      ordered.forEachIndexed { i, page ->
        rules.filter { it.first == page }
          .filter { it.second in ordered }
          .map { ordered.indexOf(it.second) }
          .filter { j -> j < i }
          .forEach { j ->
            swapIndexes(ordered, i, j)
          }
      }
    }
    return ordered
  }

  private fun swapIndexes(ordered: MutableList<Int>, i: Int, j: Int) {
    val temp = ordered[i]
    ordered[i] = ordered[j]
    ordered[j] = temp
  }
}
