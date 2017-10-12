#include <iostream>

using namespace std;

int main(){
	string a;
	cin >> a;
	string b;
	cin >> b;
	bool flag = true;
	if(a.length() != b.length()){
		flag = false;
	}else{
		int letters[128] = {0};

		for(int i=0;i<a.length();i++){
			letters[a[i]]++;
		}

		for(int i=0;i<b.length();i++){
			letters[b[i]]--;
			if(letters[b[i]] < 0){
				flag =false;
				break;
			}
		}
	}

	if(flag){
        cout << "the strings "<<a<<" and "<<b<<" are permutations of each other";
    }else{
        cout << "the strings "<<a<<" and "<<b<<" are not permutations of each other";
    }

	return 0;
}
