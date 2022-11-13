#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

unsigned long long int binomialCoefficients(int n, int k) {
	unsigned long long int C[k+1];
	memset(C, 0, sizeof(C));
	C[0] = 1;
	for (int i = 1; i <= n; i++) {
		for (int j = fmin(i, k); j > 0; j--)
			C[j] = C[j] + C[j-1];
		}
	return C[k];
}

int main(int argc, const char *argv[]){
	FILE *save_file = fopen("pascaltree.txt", "w");
	if (!save_file)
		return -1;
	if (argc > 1){
		int n = atoi(argv[1]);
		fprintf(save_file, "%d\n", n);
		for (int i=0; i < n; i++){
			for (int j=0; j <= i; j++){
				fprintf(save_file, "%llu ", binomialCoefficients(i, j));
			}
			fprintf(save_file, "\n");
		}
	}

	fclose(save_file);

	return 0;
}
