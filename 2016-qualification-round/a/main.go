package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// evalUniqueness can be 1 ~ 3.
// If s[idx] is same as s[idx-1] *and* s[idx+1], it returns 1
// If s[idx] is same as s[idx-1] *or* s[idx+1], it returns 2
// If s[idx] is different from both s[idx-1] and s[idx+1], it returns 3
// Condition: len(s) >= 1
func evalUniqueness(s string, idx int) int {
	uniqueness := 1
	if idx > 0 {
		if s[idx-1] != s[idx] {
			uniqueness++
		}
	}
	if idx < len(s)-1 {
		if s[idx+1] != s[idx] {
			uniqueness++
		}
	}
	return uniqueness
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	_, _ = reader.ReadString('\n') // Discard first line

	for i := 1; ; i++ {
		uniqueness := 1
		text, err := reader.ReadString('\n')
		text = strings.TrimRight(text, "\n")
		if err != nil {
			// fmt.Println("Reached to EOF")
			break
		}
		for j := 0; j < len(text); j++ {
			uniqueness *= evalUniqueness(text, j)
		}
		fmt.Printf("Case #%d: %d\n", i, uniqueness)
	}
}
