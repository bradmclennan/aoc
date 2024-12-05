class Day4 : Day(4) {
  override fun getPart1(): Any = getRows().let { countStringInRows(it, "XMAS") }

  private fun getRows(): List<List<String>> = getLines(getFilename(1)).map { it.toCharArray().map(Char::toString) }

  private fun countStringInRows(rows: List<List<String>>, string: String): Int {
    val stringBackwards = string.reversed()
    val horizontal = getHorizontal(rows, string)
    val vertical = getVertical(rows, string)
    val diagonalUp = getDiagonalUp(rows, string)
    val diagonalDown = getDiagonalDown(rows, string)
    val horizontalBackwards = getHorizontal(rows, stringBackwards)
    val verticalBackwards = getVertical(rows, stringBackwards)
    val diagonalUpBackwards = getDiagonalUp(rows, stringBackwards)
    val diagonalDownBackwards = getDiagonalDown(rows, stringBackwards)
    return horizontal + vertical + diagonalUp + diagonalDown + horizontalBackwards + verticalBackwards + diagonalUpBackwards + diagonalDownBackwards
  }


  private fun getVertical(rows: List<List<String>>, string: String): Int = rows.drop(3).mapIndexed { j, row ->
    row.filterIndexed { i, _ -> rows[j][i] + rows[j + 1][i] + rows[j + 2][i] + rows[j + 3][i] == string }.count()
  }.sum()

  private fun getHorizontal(rows: List<List<String>>, string: String): Int = rows.sumOf {
    it.dropLast(3).filterIndexed { i, _ ->
      it.subList(i, i + 4).joinToString(separator = "") == string
    }.count()
  }

  private fun getDiagonalUp(rows: List<List<String>>, string: String): Int = rows.drop(3).mapIndexed { j, row ->
    row.dropLast(3)
      .filterIndexed { i, _ ->
        rows[j + 3][i] + rows[j + 3 - 1][i + 1] + rows[j + 3 - 2][i + 2] + rows[j + 3 - 3][i + 3] == string
      }
      .count()
  }.sum()

  private fun getDiagonalDown(rows: List<List<String>>, string: String): Int = rows.dropLast(3).mapIndexed { j, row ->
    row.dropLast(3)
      .filterIndexed { i, _ ->
        rows[j][i] + rows[j + 1][i + 1] + rows[j + 2][i + 2] + rows[j + 3][i + 3] == string
      }
      .count()
  }.sum()

  override fun getPart2(): Any = getRows().let(::getCrossCount)

  private fun getCrossCount(rows: List<List<String>>): Int =
    rows.drop(1).dropLast(1)
      .mapIndexed { j, row ->
        row.drop(1).dropLast(1).filterIndexed { i, col -> isCrossColumn(i, j, rows, col) }.count()
      }.sum()

  private fun isCrossColumn(
    i: Int,
    j: Int,
    rows: List<List<String>>,
    col: String
  ): Boolean {
    val x = i + 1
    val y = j + 1
    val corners = listOf(
      rows[y - 1][x - 1],
      rows[y - 1][x + 1],
      rows[y + 1][x - 1],
      rows[y + 1][x + 1]
    )
    return col == "A" && corners.let(::isCross)
  }

  private fun isCross(corners: List<String>) =
    (corners[0] + corners[1] + corners[2] + corners[3]) in listOf("SSMM", "MMSS", "MSMS", "SMSM")
}
