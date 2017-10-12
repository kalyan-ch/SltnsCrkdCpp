#include <iostream>

using namespace std;

int main(){

	string word;
	cin >> word;
	int letters[128] = {0};
	bool flag = true;

	for (int i = 0; i < word.length(); i++){
		letters[word[i]]++;
	}

	if( word.length()%2 == 0 ){
		for (int i = 0; i < 128; i++){
			if(letters[i]%2 != 0){
				flag = false;
				break;
			}
		}

	}else{
		int oddCount = 0;
		for (int i = 0; i < 128; i++){
			if(letters[i]%2 != 0){
				oddCount++;
				if( oddCount > 1){
					flag = false;
					break;
				}
			}
		}
	}

	if(flag){
        cout << "Some permutations of the string are palindromes";
    }else{
        cout << "No permutation of the string is a palindrome";
    }

	return 0;
}
