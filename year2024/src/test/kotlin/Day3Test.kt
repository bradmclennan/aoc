import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

class Day3Test {

  @Test
  fun `should get sum of multiplications`() {
    assertEquals(161, Day3().getPart1())
  }

  @Test
  fun `should get sum of enabled multiplications `() {
    assertEquals(48, Day3().getPart(2))
  }

}