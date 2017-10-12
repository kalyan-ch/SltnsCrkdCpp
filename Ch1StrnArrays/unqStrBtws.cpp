#include <iostream>

using namespace std;


int main()
{
	string a;
	cin >> a;
	int checker = 0;
	bool flag = true;
	for (int i=0; i<a.length();i++){
		int val = a[i]-'a';
		if( (checker & (1<<val)) > 0){
			flag = false;
			break;
		}

		checker = checker | (1<<val);
	}

	if(flag){
		cout << "the string "<<a<<" is made of unique characters";
	}else{
		cout << "the string "<<a<<" is not made of unique characters";
	}

	return 0;
}
