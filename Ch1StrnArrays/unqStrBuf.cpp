#include <iostream>

using namespace std;

int main(){
	string a;
	cin >> a;
	bool flag = true;
	bool dup_arr[128] = {false};
	for (int i=0; i<a.length();i++){
		if(dup_arr[a[i]]){
			flag = false;
			break;
		}

		dup_arr[a[i]] = true;
	}

	if(flag){
		cout << "the string "<<a<<" is made of unique characters";
	}else{
		cout << "the string "<<a<<" is not made of unique characters";
	}
	
	return 0;
}