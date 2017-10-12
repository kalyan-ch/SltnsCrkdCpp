#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int firstDuplicate(vector<int> a){
	
	int index = -1;
	for(int i=0;i<a.size();i++){
		if(a[abs(a[i-1])]<0){
			index = i;
			break;
		}else{
			a[a[i-1]] = (-1)*a[a[i-1]];	
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