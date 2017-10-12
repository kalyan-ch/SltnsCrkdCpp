#include <iostream>
#include <cstdlib>

using namespace std;

void printMatrix(int mtrx[][n],int n){
	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			cout << mtrx[i][j] << " ";
		}
		cout << endl;
	}
}

void rotateMatrix(int mtrx[][n], int n){
    for(int layer=0;layer<n/2;layer++){
    	int first = layer;
    	int last = n-layer-1;
    	for (int i = first; i < last; ++i){
    		int off = i-first;
    		int temp = mtrx[first][i];
    		mtrx[first][i] = mtrx[last-off][first];
    		mtrx[last-off][first] = mtrx[last][last-off];
    		mtrx[last][last-off] = mtrx[i][last];
    		mtrx[i][last] = temp;
    	}
    }
}


int main(){
    int n = 4;
	int mtrx[n][n];

	for (int i = 0; i < n; ++i){
		for (int j = 0; j < n; ++j){
			mtrx[i][j] = rand()%15+1;
		}
	}

	printMatrix(mtrx,n);
	rotateMatrix(mtrx,n);
	printMatrix(mtrx,n);

	return 0;
}
