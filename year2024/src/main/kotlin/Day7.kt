class Day7 : Day(7) {
  override fun getPart1(): Any = testValues(getLines(getFilename(1))).let(::getSumOfTestValues)

  private fun testValues(lines: List<String>) =
    lines
      .map(::parseLineToTestValue)
      .filter(::isCorrectTestValue)

  private fun parseLineToTestValue(line: String) =
    Regex("\\d+")
      .findAll(line)
      .map(MatchResult::value)
      .map(String::toDouble)
      .toList()
      .let { it.first() to it.drop(1) }

  private fun isCorrectTestValue(testValue: Pair<Double, List<Double>>): Boolean {
    if (testValue.second.size > 2) {
      val last = testValue.second.last()
      val list = testValue.second.dropLast(1)
      return isCorrectTestValue(testValue.first.minus(last) to list)
          || isCorrectTestValue(testValue.first.div(last) to list)
    }
    val isAdd = testValue.first == testValue.second.sum()
    val isMultiply = testValue.first == testValue.second.reduce(Double::times)
    return isAdd || isMultiply
    // 10 * 19
    // 19 + 19
    // 2 items = 2 results = 2^(n-1) = 2^1

    //   190
    //    10
    // *19  +19

    // 81 * 40 * 27
    // 81 * 40 + 27 (correct)
    // 81 + 40 * 27 (correct)
    // 81 + 40 + 27
    // 3 items = 4 results = 2^(n-1) = 2^2

    //           3267
    //            81
    //     *40         +40
    //  *27   +27   *27   +27

    // 11 * 6 * 16 * 20
    // 11 * 6 * 16 + 20
    // 11 * 6 + 16 + 20
    // 11 * 6 + 16 * 20
    // 11 + 6 * 16 * 20
    // 11 + 6 * 16 + 20
    // 11 + 6 + 16 + 20
    // 11 + 6 + 16 * 20
    // 4 items = 8 results = 2^(n-1) = 2^3
  }

  private fun getSumOfTestValues(testValues: List<Pair<Double, List<Double>>>) =
    testValues.sumOf { it.first.toLong() }

  override fun getPart2(): Any {
    return 0
  }
}
