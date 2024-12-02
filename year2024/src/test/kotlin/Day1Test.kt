import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

class Day1Test {
  @Test
  fun `should get sum of distances`() {
    assertEquals(11L, Day1().getSumOfDistances("day1/part1.txt"))
  }

  @Test
  fun `should get similarity score`() {
    assertEquals(31L, Day1().getSimilarityScore("day1/part1.txt"))
  }
}