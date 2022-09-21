#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN 50
int N;

struct ST{
    char str[51];
    int len;
};

int comp(const void* a, const void* b){
    struct ST *x = (struct ST*)a;
    struct ST *y = (struct ST*)b;
    if (x->len < y->len) return -1;
    else if(x->len > y->len) return 1;
    return strcmp(x->str, y->str);
}

int main(){
    scanf("%d", &N);
    struct ST A[N];

    for(int i=0; i<N; i++){
        scanf("%s", A[i].str);
        A[i].len = strlen(A[i].str);
    }
    
    qsort(A, N, sizeof(A[0]), comp);

    printf("%s\n", A[0].str);
    for(int i=1; i<N; i++){
        if (strcmp(A[i].str, A[i-1].str))
            printf("%s\n", A[i].str);
    }
    //OutputData();
    return 0;
}