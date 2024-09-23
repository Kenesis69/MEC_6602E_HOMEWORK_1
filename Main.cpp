
#include <iostream>
#include <vector>
using namespace std; 
constexpr double pi = 3.14159265358979323846;

class Maillage{
public:


    //variable
    double x1,x2;
    int n;


    //constructor
    Maillage(double a, double b, int c) : x1(a), x2(b), n(c) {
    cout <<"********************** MAILLAGE *****************************" << std::endl;
    cout <<"beginning x = "<< Maillage::x1 << std::endl;
    cout <<"end x = "<< Maillage::x2 << std::endl;
    cout <<"number of nodes n = "<< Maillage::n << std::endl;
    }; 

    
    // vector getter and printer
    std::vector<double> get_vector(){
        vector<double> result;
        double delta_x = (x2 - x1)/(n-1);
        for(int i = 0; i < n ; i++){
            result.push_back(x1 + (i)*delta_x);
        };
        cout << "Vector is: " << std::endl;
        for (int i = 0; i < result.size(); i++) {
            cout << result.at(i) << " ";  
        }
        cout << endl;
        return result;
    };
};

class Solveur{
public:
    Maillage Maillage_to_use;
    string method;

    // Constructor
    Solveur (Maillage a, string b) : Maillage_to_use(a), method(b) {
    cout <<"********************** SOLVEUR *****************************" << std::endl;
    cout << "Maillage used :" << endl;
    Maillage_to_use.get_vector();
    };

    std::vector<std::vector<double>> Solve() {
    // Initialize a 2x2 matrix with all elements set to 0
        std::vector<std::vector<double>> matrix(2, std::vector<double>(2, 0));

    // Optionally, perform some matrix operations (currently it just returns an empty matrix)

    return matrix; // Return the matrix
    };
};

//Main
int main(){
    //definition parameters
    double c = 0.5; //constant c
    double x1 = 0; // beginning
    double x2  = pi ; // end
    int n = 5; // number of point
    std::string method = "implicit";

    double delta_x = (x2 - x1)/(n-1); //delta_x calculated
    double delta_t = 0.5; //delta_t 
    double CFL = (c*delta_t)/delta_x; // CFL calculated
    cout <<"********************** PARAMETERS ***************************" << std::endl;
    cout<< "The CFL is:  "<<CFL << std::endl; 


    //
    Maillage Maillage_devoir(x1,x2,n); // declaration object maillage
    vector<double> ligne = Maillage_devoir.get_vector(); //getting vector for solver
    
    Solveur Solveur_Devoir(Maillage_devoir,method);
    Solveur_Devoir.Solve();

    cout << endl;
    return 0;
    
};