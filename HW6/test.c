#include <stdio.h>

int power(int in_a, int m) {
	int i, out_a;
	out_a = in_a;
	for (i = 0; i < m; i++)
		out_a = out_a * in_a;
	return out_a;
}

int power_new(int in_b, int n) {
	int i, out_b;
	out_b = in_b;
	for (i = 0; i < n; i++)
		out_b = out_b * out_b;
	return out_b;
}

int main() {
	int i, j, k, l;
	FILE *correct = fopen("test_correct.txt", "w");
	FILE *incorrect = fopen("test_incorrect.txt", "w");
	for (i = 0; i < 10; i++) {
		for (j = 0; j < 10; j++) {
			for (k = 0; k < 10; k++) {
				for (l = 0; l < 10; l++) {
					if (power(i,j) == power_new(k,l)) {
						// Write to correct file
						fprintf(correct, "%d\n", i);
						fprintf(correct, "%d\n", j);
						fprintf(correct, "%d\n", k);
						fprintf(correct, "%d\n", l);
					} else {
						// Write to incorrect file
						fprintf(incorrect, "%d\n", i);
						fprintf(incorrect, "%d\n", j);
						fprintf(incorrect, "%d\n", k);
						fprintf(incorrect, "%d\n", l);
					}
				}
			}
		}
	}	
	fclose(correct);
	fclose(incorrect);
}