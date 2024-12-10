import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

class Day6Test {

  @Test
  fun `should get distinct guard positions`() {
    assertEquals(41, Day6().getPart1())
  }

  @Test
  fun `should get loop obstruction positions`() {
    assertEquals(6, Day6().getPart2())
  }
}