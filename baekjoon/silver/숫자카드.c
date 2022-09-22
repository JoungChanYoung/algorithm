#include<stdio.h>
#include<stdlib.h>

#define MAXN ((int)5e5)
int A[MAXN+10];
int B[MAXN+10];
int ans[MAXN+10];
int N, M;

int comp(const void* a, const void* b){
    return *(int *)a - *(int *)b;
}

int BS(int d){ //binary search
    int s, e, m;
    s = 0;
    e = N-1;
    while(s <= e){
        m = (s + e) / 2;
        if(A[m] == d) return 1;
        else if(A[m] > d) e = m - 1;
        else s = m + 1;
    }
    return 0;
}
void Solve(){
    qsort(A, N, sizeof(A[0]), comp);
    for (int i=0; i<M; i++){
        if (BS(B[i])) ans[i] = 1;
    }    
}

void InputData(){
    scanf("%d", &N);
    for(int i=0; i<N; i++){
        scanf("%d", &A[i]);
    }
    scanf("%d", &M);
    for(int i=0; i<M; i++){
        scanf("%d", &B[i]);
    }
}

int main(){
    InputData();

    Solve();

    for(int i=0; i<M; i++){
        printf("%d ",ans[i]);
    }
    return 0;
}