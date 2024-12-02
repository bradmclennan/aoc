abstract class Day(private var day: Int) {
  abstract fun getPart1(): Any
  abstract fun getPart2(): Any

  fun getFilename(part: Int): String = "day${day}/part$part.txt"

  fun print() {
    println("Day $day Part1: ${getPart1()}, Part2: ${getPart2()}")
  }
}
