import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

class Day2Test {

  @Test
  fun `should get safe report count`() {
    assertEquals(2, Day2().getPart1())
  }

  @Test
  fun `should get safe report count with problem dampener`() {
    assertEquals(4, Day2().getPart2())
  }
}