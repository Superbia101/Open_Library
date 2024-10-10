// Выводит число под необходимым номером из последовательности Фибоначчи.
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin) // подготавливаем считывание
	fmt.Print("Число Фибоначчи №: ")
	input, err := reader.ReadString('\n') // читаем данные введёные пользователем до нажатия Enter

	if err != nil { // проверка на ошибки
		log.Fatal(err)
	}

	input = strings.TrimSpace(input) // удаляем Enter
	num, err := strconv.Atoi(input)  // преобразуем сторку в целое число

	if err != nil { // проверка на ошибки
		log.Fatal(err)
	}
	a, b := 1, 1
	for i := 2; i < num; i++ {
		a, b = a+b, a
	}
	fmt.Print("Число №", num, " равно: ", a)
}
