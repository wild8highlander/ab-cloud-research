package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	zerosN := flag.Int("zeros", 10000, "number of zeros to load")
	source := flag.String("source", "auto", "data source: auto|50000|500k|2M|highT|zeros6")
	objection := flag.String("objection", "all", "objection to run: 1|2|3|all")
	lang := flag.String("lang", "en", "output language: en|ru")
	flag.Parse()

	dataDir := filepath.Join("..", "data")

	fmt.Println()
	fmt.Println("  ╔═══════════════════════════════════════════════════════╗")
	fmt.Println("  ║        AB-Cloud Verification Suite  (Go)             ║")
	fmt.Println("  ╚═══════════════════════════════════════════════════════╝")
	fmt.Println()
	fmt.Printf("  Config: zeros=%d  source=%s  objection=%s  lang=%s\n\n", *zerosN, *source, *objection, *lang)

	zeros, err := LoadZeros(dataDir, *zerosN, *source)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error loading zeros: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("  Loaded %d zeros from source '%s'.\n\n", len(zeros), *source)

	runObj := func(id int) {
		switch *lang {
		case "ru":
			switch id {
			case 1:
				fmt.Println(Objection1RU(zeros))
			case 2:
				fmt.Println(Objection2RU(zeros))
			case 3:
				fmt.Println(Objection3RU(zeros))
			}
		default:
			switch id {
			case 1:
				fmt.Println(Objection1EN(zeros))
			case 2:
				fmt.Println(Objection2EN(zeros))
			case 3:
				fmt.Println(Objection3EN(zeros))
			}
		}
	}

	switch strings.ToLower(*objection) {
	case "1":
		runObj(1)
	case "2":
		runObj(2)
	case "3":
		runObj(3)
	case "all":
		runObj(1)
		runObj(2)
		runObj(3)
	default:
		fmt.Fprintf(os.Stderr, "Unknown objection: %s (use 1, 2, 3, or all)\n", *objection)
		os.Exit(1)
	}

	fmt.Println()
	fmt.Println("  ══════════════════════════════════════════════════════")
	fmt.Println("  AB-Cloud Verification Suite — complete.")
	fmt.Println()
}
