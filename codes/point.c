#include <stdio.h>

void point(double A[], double B[], double C[], double n) {
    for (int i = 0; i < 2; i++) {
        C[i] = (A[i] + B[i] * n) / (n + 1);
    }
}



