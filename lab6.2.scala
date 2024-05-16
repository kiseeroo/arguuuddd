object Main extends App {
  // Function to filter numbers greater than the base
  def filterGreaterThanBase(input: Array[Int], base: Int): Array[Int] = {
    input.filter(_ > base)
  }

  // Function to check if a number is a Daffodil number
  def isDaffodil(n: Int): Boolean = {
    val digits = n.toString.map(_.asDigit)
    val power = digits.length
    val sum = digits.map(math.pow(_, power)).sum.toInt
    sum == n
  }

  // Overloaded function to check Daffodil numbers for two inputs
  def isDaffodil(x: Int, y: Int): (Boolean, Boolean) = {
    (isDaffodil(x), isDaffodil(y))
  }

  // Function to count the occurrences of each letter in a string
  def countLetters(input: String, counts: Map[Char, Int]): Map[Char, Int] = {
    input.foldLeft(counts)((acc, char) => acc + (char -> (acc.getOrElse(char, 0) + 1)))
  }

  // Example usage of the functions
  val base = 12
  val inputArray = Array(5, 21, 17, 4, 10, 15)
  val inputString = "aadabcbbbcc"
  
  println("Filtered numbers greater than base:")
  val filteredNumbers = filterGreaterThanBase(inputArray, base)
  println(filteredNumbers.mkString(","))

  println("\nIs Daffodil number:")
  val result1 = isDaffodil(200)
  val result2 = isDaffodil(0)
  println(s"200: $result1, 0: $result2")

  println("\nCount of letters:")
  val initialCounts = Map.empty[Char, Int]
  val letterCounts = countLetters(inputString, initialCounts)
  println(letterCounts)
}
