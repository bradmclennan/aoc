import kotlin.math.absoluteValue

class Day2 : Day(2) {
  override fun getPart1(): Any = getSafeReportCount(getFilename(1), false)

  override fun getPart2(): Any = getSafeReportCount(getFilename(1), true)

  private fun getSafeReportCount(filename: String, dampener: Boolean): Int = getLines(filename)
    .map { getReport(it) }
    .count { levels ->
      isSafe(levels)
          || (dampener && List(levels.size) { levels.filterIndexed { index, _ -> index != it } }.any { isSafe(it) })
    }

  private fun getReport(it: String) =
    Regex("\\d+")
      .findAll(it)
      .toList()
      .map(MatchResult::value)
      .map(String::toInt)

  private fun isSafe(levels: List<Int>): Boolean {
    val sorted = levels.sorted()
    val isIncreasing = levels == sorted
    val isDecreasing = levels == sorted.reversed()
    val isNotSorted = !isIncreasing && !isDecreasing
    if (isNotSorted) return false
    return levels.dropLast(1)
      .mapIndexed { index, it -> getDifference(it to levels[index + 1]) }
      .none { it < 1 || it > 3 }
  }

  private fun getDifference(levelPair: Pair<Int, Int>): Int = (levelPair.first - levelPair.second).absoluteValue

}