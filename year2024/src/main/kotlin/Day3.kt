class Day3 : Day(3) {

  override fun getPart1(): Any =
    getLines(getFilename(1))
      .joinToString(separator = "")
      .let {
        getMultipliedPairs(it, false)
      }.let {
        getSumOfMultipliedPairs(it)
      }

  private fun getMultipliedPairs(corruptedMemory: String, operationsEnabled: Boolean) =
    Regex("mul\\((\\d+),(\\d+)\\)|(don't\\(\\)|do\\(\\))")
      .findAll(corruptedMemory)
      .let {
        var enabled = true
        it.fold(emptyList<MatchResult>()) { acc, match ->
          when (match.value) {
            "do()" -> {
              enabled = true
              acc
            }

            "don't()" -> {
              enabled = false
              acc
            }

            else -> {
              if (enabled || !operationsEnabled) acc.plus(match) else acc
            }
          }
        }
      }
      .map { it.groups.drop(1) }
      .map { it.filterNotNull().map(MatchGroup::value).map(String::toInt) }
      .map { it[0] to it[1] }
      .toList()

  private fun getSumOfMultipliedPairs(multipliedPairs: List<Pair<Int, Int>>) =
    multipliedPairs.sumOf { it.first.times(it.second) }

  override fun getPart2(): Any =
    getPart(1)

  fun getPart(part: Int) = getLines(getFilename(part))
    .joinToString(separator = "")
    .let {
      getMultipliedPairs(it, true)
    }.let {
      getSumOfMultipliedPairs(it)
    }
}