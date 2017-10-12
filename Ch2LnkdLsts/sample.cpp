#include <iostream>
#include <vector>

using namespace std;

int pop(vector<int> *v){
	int num = v->back();
	return num;
}

int main(){
	vector<int> v;

	for (int i = 0; i <= 9; ++i){
		v.push_back(i);
	}
	for (int i = 0; i <= 9; ++i){
		cout<<pop(&v)<<endl;
	}
	return 0;
}
