#include <iostream>

using namespace std;

int main(){
	string s;
	cin >> s;
	int count = 0;
	char;
	for(int i=0;i<s.length();i++){
		count++;
		if((i+1)>s.length() || s[i]!=s[i+1]){
			string cnt = string(intStr);
			cout<<cnt<<endl;
			s1 += s[i]+cnt;
			count = 0;
		}
	}

	(s1.length()<s.length())?cout<<s1<<endl:cout<<s<<endl;

	return 0;
}

