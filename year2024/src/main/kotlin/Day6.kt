import java.awt.Point

class Day6 : Day(6) {
  override fun getPart1(): Any {
    val map = patrolMap(getMap())
    return countMapVisits(map)
  }

  private fun countMapVisits(map: List<List<String>>) =
    map.flatten().count { it == "X" }

  private fun isPatrolLoop(map: List<List<String>>) =
    map.any { "-" in it }

  private fun patrolMap(map: List<MutableList<String>>): List<List<String>> {
    var guard: Point? = getGuardPoint(map)
    val direction = Point(0, -1)
    val moves = HashSet<Pair<Point, Point>>()
    while (guard != null) {
      val currentMove = Point(guard) to Point(direction)
      if (currentMove in moves) {
        map[guard.y][guard.x] = "-"
        break
      }
      moves += currentMove
      moveGuard(map, guard, direction)
      guard = checkGuardMapBounds(guard, map)
    }
    return map
  }

  private fun checkGuardMapBounds(
    guard: Point,
    map: List<MutableList<String>>
  ): Point? = when {
    guard.x !in 0 until map[0].size -> null

    guard.y !in map.indices -> null

    else -> guard
  }

  private fun moveGuard(
    map: List<MutableList<String>>,
    guard: Point,
    direction: Point
  ) {
    map[guard.y][guard.x] = "X"
    if (isGuardBlocked(guard, direction, map)) {
      val rotateDirection = rotateDirection(direction)
      direction.x = rotateDirection.x
      direction.y = rotateDirection.y
    }
    guard.x += direction.x
    guard.y += direction.y
  }

  private fun isGuardBlocked(
    guard: Point,
    direction: Point,
    map: List<MutableList<String>>
  ): Boolean {
    val inXBounds = guard.x + direction.x in 0 until map[0].size
    val inYBounds = guard.y + direction.y in map.indices
    if (!inXBounds || !inYBounds) {
      return false
    }
    return map[guard.y + direction.y][guard.x + direction.x] == "#"
  }

  private fun rotateDirection(direction: Point): Point = when (direction) {
    Point(0, 1) -> Point(-1, 0)
    Point(-1, 0) -> Point(0, -1)
    Point(0, -1) -> Point(1, 0)
    else -> Point(0, 1)
  }

  private fun getGuardPoint(map: List<List<String>>): Point =
    Point(map.flatten().indexOfFirst { it.contains("^") } % map[0].size, map.indexOfFirst { it.contains("^") })

  private fun getMap(): List<MutableList<String>> =
    getLines(getFilename(1)).map { it.split("").filter(String::isNotBlank).toMutableList() }.toList()

  override fun getPart2(): Any {
    return 0
    var count = 0
    val map = getMap()
    map.forEachIndexed { j, row ->
      row.forEachIndexed { i, col ->
        if (
          map.toList().map { it.toMutableList() }.takeIf { col != "^" }?.also { it[j][i] = "#" }?.let { patrolMap(it) }
            ?.let { isPatrolLoop(it) } == true) {
          count++
        }
      }
    }
    return count
  }

}