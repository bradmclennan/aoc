import kotlin.math.absoluteValue


class Day1 : Day(1) {

  override fun getPart1(): Long {
    return getSumOfDistances(getFilename(1))
  }

  fun getSumOfDistances(filename: String): Long =
    getLines(filename)
      .let { getLists(it) }
      .let { getSmallestPairs(it) }
      .let { getSumOfDistances(it) }

  private fun getLines(filename: String): List<String> = this.javaClass.getResource(filename)!!.readText().lines()

  private fun getSmallestPairs(lists: Pair<List<Long>, List<Long>>): List<Pair<Long, Long>> =
    List(lists.first.size) { index ->
      getSmallestPairOfIndex(index, lists)
    }

  private fun getSmallestPairOfIndex(i: Int, lists: Pair<List<Long>, List<Long>>): Pair<Long, Long> =
    lists.first.sorted()[i] to lists.second.sorted()[i]

  private fun getLists(lines: List<String>): Pair<List<Long>, List<Long>> = lines.map { getPair(it) }.let { pairs ->
    Pair(pairs.map { it.first }, pairs.map { it.second })
  }

  private fun getSumOfDistances(pairs: List<Pair<Long, Long>>): Long =
    pairs.sumOf { getDistance(it) }

  private fun getPair(line: String): Pair<Long, Long> =
    Regex("\\d+").findAll(line).toList().map(MatchResult::value).map(String::toLong).let { it.first() to it.last() }

  private fun getDistance(pair: Pair<Long, Long>): Long = pair.first.minus(pair.second).absoluteValue

  override fun getPart2(): Long {
    return getSimilarityScore(getFilename(1))
  }

  fun getSimilarityScore(filename: String): Long =
    getLines(filename)
      .let { getLists(it) }
      .let {
        it.first.sumOf { number -> getSimilarityScore(number, getFrequency(number, it.second)) }
      }

  private fun getFrequency(number: Long, list: List<Long>): Long = list.count { it == number }.toLong()

  private fun getSimilarityScore(number: Long, frequency: Long) = number * frequency
}