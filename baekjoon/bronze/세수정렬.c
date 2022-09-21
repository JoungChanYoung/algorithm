#include<stdio.h>
#include<stdlib.h>

#define N 3
int A[N];

int comp(const void* a, const void* b){
    return *(int *)a - *(int *)b;
}

void InputData(){
    for(int i=0; i<3; i++) scanf("%d", &A[i]);
}

void OutputData(){
    for(int i=0; i<3; i++) printf("%d ", A[i]);
}

int main(){
    int ans = 0;

    InputData();

    qsort(A, N, sizeof(A[0]), comp);

    OutputData();

    return 0;
}