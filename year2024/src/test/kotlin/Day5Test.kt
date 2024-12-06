import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

class Day5Test {

  @Test
  fun `should add up middle page numbers of correctly ordered updates`() {
    assertEquals(143, Day5().getPart1())
  }

  @Test
  fun `should add up middle page numbers of ordered incorrect updates`() {
    assertEquals(123, Day5().getPart2())
  }
}