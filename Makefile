## output : Compute prime numbers

.PHONY : outputs
outputs : results/output.txt results/outputs_.txt

results/output.txt : input.txt
	python calculate_primes.py input.txt results/output.txt
    
results/output_.txt : input_.txt
	python calculate_primes.py input_.txt results/output_.txt
    
## clean : clean outputs
.PHONY : clean
clean :
	rm results/*
	
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<