package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

func main() {
	zerosN := flag.Int("zeros", 50000, "number of zeros to load")
	source := flag.String("source", "auto", "data source: auto|50k|50k_full|500k|2M|highT|csv|zeros6")
	objection := flag.String("objection", "all", "objection to run: 1|2|3|all")
	lang := flag.String("lang", "en", "output language: en|ru")
	dataDir := flag.String("data-dir", "../data", "path to the data directory")
	noSC := flag.Bool("no-selfcheck", false, "skip the frozen-anchor self-check")
	flag.Parse()

	fmt.Println()
	fmt.Println("  ╔═══════════════════════════════════════════════════════╗")
	fmt.Println("  ║        AB-Cloud Verification Suite  (Go)             ║")
	fmt.Println("  ╚═══════════════════════════════════════════════════════╝")
	fmt.Println()
	fmt.Printf("  Config: zeros=%d  source=%s  objection=%s  lang=%s\n\n", *zerosN, *source, *objection, *lang)

	zeros, err := LoadZeros(*dataDir, *zerosN, *source)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error loading zeros: %v\n", err)
		os.Exit(2)
	}
	fmt.Printf("  Loaded %d zeros from source '%s'.\n\n", len(zeros), *source)

	if len(zeros) < 2 {
		fmt.Fprintln(os.Stderr, "ERROR: need at least 2 zeros.")
		os.Exit(2)
	}

	scFail := -1
	if !*noSC {
		rows, nPass, nFail := Selfcheck(zeros)
		if *lang == "ru" {
			fmt.Print(RenderSelfcheckRU(rows, nPass, nFail))
		} else {
			fmt.Print(RenderSelfcheckEN(rows, nPass, nFail))
		}
		scFail = nFail
	}

	runObj := func(id int) {
		if *lang == "ru" {
			switch id {
			case 1:
				fmt.Print(RenderObj1RU(RunObjection1(zeros)))
			case 2:
				fmt.Print(RenderObj2RU(RunObjection2(zeros)))
			case 3:
				fmt.Print(RenderObj3RU(RunObjection3(zeros)))
			}
		} else {
			switch id {
			case 1:
				fmt.Print(RenderObj1EN(RunObjection1(zeros)))
			case 2:
				fmt.Print(RenderObj2EN(RunObjection2(zeros)))
			case 3:
				fmt.Print(RenderObj3EN(RunObjection3(zeros)))
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
		os.Exit(2)
	}

	fmt.Println()
	fmt.Println("  ══════════════════════════════════════════════════════")
	fmt.Println("  AB-Cloud Verification Suite — complete.")
	fmt.Println()

	if scFail > 0 {
		os.Exit(1)
	}
}
