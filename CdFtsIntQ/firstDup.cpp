#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int firstDuplicate(vector<int> a){
	vector<int> a1(a.size());
	int index = -1;
	for(int i=0;i<a.size();i++){
		int num = a[i];
		if(a1[num-1]==0){
			a1[num-1]=1;
		}else{
			index = i;
			break;
		}
	}

	if(index>-1){
		return a[index];	
	}else{
		return index;
	}
	
}

int main(){

	vector <int> a;
	a.push_back(2);
	a.push_back(3);
	a.push_back(3);
	a.push_back(5);
	a.push_back(1);
	a.push_back(2);

	cout << firstDuplicate(a);
}