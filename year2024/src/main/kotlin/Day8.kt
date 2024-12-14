import java.awt.Point

class Day8 : Day(8) {
  override fun getPart1(): Any {
    val lines = getLines(getFilename(1))
    return lines.mapIndexed { row, line -> getLinePoints(line, row) }
      .flatten().also {
//        printLocations(it.toSet(), lines[0].length, lines.size)
      }
      .let { getLocations(it, lines[0].length, lines.size) }
      .let { getUniqueLocations(it, lines[0].length, lines.size) }
  }

  private fun getUniqueLocations(locations: List<Pair<String, Point>>, width: Int, height: Int) =
    locations.toSet().also {
//      printLocations(it, width, height)
    }
      .filter { it.first == "#" }
      .size

  private fun printLocations(it: Set<Pair<String, Point>>, width: Int, height: Int) {
    (0 until height).forEach { row ->
      (0 until width).forEach { column ->
        it.firstOrNull { location -> location.second.x == column && location.second.y == row }?.let { print(it.first) }
          ?: print(".")
      }
      print("\n")
    }
    print("\n")
  }

  private fun getLocations(
    antennaPoints: List<Pair<String, Point>>,
    width: Int,
    height: Int
  ): List<Pair<String, Point>> =
    antennaPoints.flatMap { i ->
      antennaPoints
        .filter { it.first == i.first }
        .filter { it != i }
        .map { j ->
          "#" to Point(i.second.x + (i.second.x - j.second.x), i.second.y + (i.second.y - j.second.y)).also {
//            println("$i -> $it")
          }
        }.plus(i)
    }
      .filter { inMapRange(it.second, width, height) }

  private fun inMapRange(it: Point, width: Int, height: Int): Boolean =
    it.x in 0 until width && it.y in 0 until height

  private fun getLinePoints(line: String, row: Int): List<Pair<String, Point>> =
    Regex("[A-z|0-9]").findAll(line).map { it.value to Point(it.range.first, row) }.toList()

  override fun getPart2(): Any {
    return 0
  }
}