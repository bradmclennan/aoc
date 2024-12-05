import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

class Day4Test {

  @Test
  fun `should count word`() {
    assertEquals(18, Day4().getPart1())
  }

  @Test
  fun `should get number of crosses`() {
    assertEquals(9, Day4().getPart2())
  }

}