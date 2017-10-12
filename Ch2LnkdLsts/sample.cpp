#include <iostream>

using namespace std;

int recursEx(int num){
    if(num==0){
        return 0;
    }
    recursEx(num-1);
	cout << "number now: " << num << "\n";
	return num-1;
}

int main(){
	recursEx(10);
	return 0;
}
