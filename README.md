# suppression-test-python-mypy

This repository is used to test our analysis code for studying suppressed warnings.
The focus here is on
 * Python repositories
 * the Mypy linter
 * the histories of individual suppression

## Expected output of our analysis scripts

*TODO: Turn this into an automatically testable format, e.g., an expected JSON file*

* Suppression 1) "# type: ignore" 
  * Introduced in commit 5ae80ba (been added while file added)
  * Code around changed (suppression line changed) in commit 60b48d5
  * Removed in commit f64b915
    
* Suppression 2) "# type: ignore[return-value]"
  * Introduced in commit f64b915
  * (Never removed)
    
*Change suppression 1) to 2) in commit f64b915. --> Change to the correct warning type.*

* Suppression 3) "# type: ignore[assignment]"
  * Introduced in commit 84a82b0
  * Code changed in the same line (but suppression is not changed) in commit 06d4370
  * Removed in commit f64b915
 
* Suppression 4) "# type: ignore[arg-type]"
  * Introduced in commit f64b915
  * (Never removed)
  
*Change suppression 3) to 4) in commit f64b915. --> Change to the correct warning type.*

* Suppression 5) "# type: ignore[attr-defined]"
  * Introduced commit 84a82b0 (initial location: src/person/person.py line 8)
  * Removed in commit f64b915
    
* Suppression 6) "# type: ignore[attr-defined]"
  * Introduced commit 84a82b0 (initial location: src/person/person.py line 9)
  * Removed in commit 06d4370 (special case: what really happens in the code is combine suppression in lines 8 and 9 into one.)
