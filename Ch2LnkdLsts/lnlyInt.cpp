
#include <vector>
#include <iostream>


using namespace std;

int getPos(long *bitV){
	long i = 1;
    int pos=1;
	while (!(i & (*bitV))){
        i = i << 1;
        ++pos;
    }
    return pos;
}

int lonely_integer(vector < int > a,int n) {
    
    if(n == 1){
    	return a[0];
    }
    long bitVec = 0;
    long bitVec2 = 0;
    long mask = 1;

    for(int i=0;i<n;i++){
    	if(a[i] > 63){
    		bitVec2 = bitVec2 ^ (mask<<(a[i]-64));
    	}else{
    		bitVec = bitVec ^ (mask<<a[i]-1);
    	}   
    }

    if(bitVec == 0){
    	return getPos(&bitVec2)+63;
    }else{
    	return getPos(&bitVec);
    }

    return 0;
}

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
       cin >> a[a_i];
    }
    cout << lonely_integer(a,n) << endl;
    return 0;
}
