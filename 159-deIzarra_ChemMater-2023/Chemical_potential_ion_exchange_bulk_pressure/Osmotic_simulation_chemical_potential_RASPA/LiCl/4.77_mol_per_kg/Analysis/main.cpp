#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <vector>
#include <math.h>
#include <sstream>

using namespace std;

#define KT 2.494338785 // in kJ/mol
#define SQR(x) x*x

double Error(vector<double> my_vector, double average);

int main(void) 
{
	int number_pressure = 20;
	
	vector<string> pressure(number_pressure,"");
	
	pressure[0]="0.006MPA";	
	pressure[1]="0.01MPA";
    pressure[2]="0.05MPA";
    pressure[3]="0.1MPA";       
	pressure[4]="0.3MPA";
	pressure[5]="0.7MPA";
	pressure[6]="1MPA";
    pressure[7]="2MPA";
    pressure[8]="5MPA";
    pressure[9]="10MPA";
    pressure[10]="40MPA";         
 	pressure[11]="70MPA";
    pressure[12]="100MPA";         
 	pressure[13]="200MPA";
    pressure[14]="300MPA";
    pressure[15]="400MPA";         
    pressure[16]="500MPA";
    pressure[17]="600MPA";
    pressure[18]="800MPA";
    pressure[19]="1000MPA";

	string buffer;
	
	vector<double> W_in_fonction_pressure(number_pressure,0.0);
	vector<double> error_W_in_fonction_pressure(number_pressure,0.0);
	vector<double> mu_in_fonction_pressure(number_pressure,0.0);
	vector<double> error_mu_in_fonction_pressure(number_pressure,0.0);
	
	vector<double> W;
	
	vector<int> lines(number_pressure,0);
	
	// Read in pressure file
	for(int j = 0; j < number_pressure; j++)
	{
		pressure[j] = "../"+pressure[j]+"/ProtocolWork.txt";
		
		ifstream iFS;
	
		// Load the trajectory and count lines	
		iFS.open(pressure[j].c_str());
		if(iFS)
		{
			while(getline(iFS, buffer))
			{
				lines[j]++;
			}
		}
		else
		{
			cout << "Cannot open file " << pressure[j] << endl;
		}
		
		lines[j]--; // remove the first line (which is text).
	
		iFS.close();
		iFS.clear();
		
	
		double number_1;
		double number_2;
		double number_3;
	
		W.clear();
	
		// Store quantity
		iFS.open(pressure[j].c_str());
		if(iFS)
		{
			getline(iFS, buffer);
			for(int i = 0; i < lines[j]; i++)
			{
				iFS >> number_1 >> number_2 >> number_3;
				W.push_back(number_3);
			}
		}
		else
		{
			cout << "Cannot open file " << pressure[j] << endl;;
		}
		
		iFS.close();
		iFS.clear();
	
	
		//---------------------------------//
			// Compute of protocol work
		//---------------------------------//
		
		W.resize(300);
		
		// calculate average of W
		double average_W = 0;
		for(int i = 0; i < W.size(); i++)
			average_W += W[i];
		
		average_W /= W.size();
		
		// Calculate error of W
		double error_W=0;
		error_W=Error(W,average_W);
	

		//---------------------------------//
				// Compute of mu.
		//---------------------------------//
		
		double average_mu = 0;
		double average_exp_W = 0;
		vector<double> exp_W(W.size(),0.0);
		
		double number;
		
		for(int i = 0; i < W.size(); i++)
		{
			exp_W[i] = exp(-W[i]/KT);
			average_exp_W += exp_W[i];
		}
			
		average_exp_W /= exp_W.size();	
	
		// Calculate error of W
		double error_exp_W=0;
		double error_mu=0;
		
		error_exp_W=Error(exp_W,average_exp_W);
		
		average_mu = -KT*log(129*130/(11*11)*average_exp_W);
		error_mu = KT*error_exp_W/average_exp_W;
		
		W_in_fonction_pressure[j]=average_W;
		error_W_in_fonction_pressure[j]=error_W;
		mu_in_fonction_pressure[j]=average_mu;
		error_mu_in_fonction_pressure[j]=error_mu;
	}

	// Output file.

	string output = "Results_osmostat.txt";

	ofstream oFS;
	
	oFS.open(output.c_str());
	
	if(oFS)
	{
		oFS << "osmostat: 2*H20 -> LiCl: Number of pseudo widom attemps: \t"<<endl;
		oFS << "Pressure (MPA) \t mu (kJ/mol) \t err_mu (kJ/mol) \t W (kJ/mol) \t err_W (kJ/mol)"<<endl;
		for(int j = 0; j < number_pressure; j++)
		{
			oFS <<pressure[j]<<"\t"<<mu_in_fonction_pressure[j]<<"\t"<<error_mu_in_fonction_pressure[j]<<"\t"<<W_in_fonction_pressure[j]<<"\t"<<error_W_in_fonction_pressure[j]<<endl;
		}
	}
	else
	{
		cout << "Cannot open file." << endl;
	}
	
	oFS.close();
	oFS.clear();

	
    return 0;
}

double Error(vector<double> my_vector, double average_total)
{
	int NR_BLOCKS = 5;
	
	int new_size = floor(my_vector.size()/NR_BLOCKS);
	
	vector<double> average_blocks(NR_BLOCKS,0.0);
	
	double sum_sqr=0.0;
	double sum = 0.0;
	
	for(int i = 0; i < NR_BLOCKS; i++)
	{
		for(int j = 0; j < new_size; j++)
		{
            //cout << i*new_size+j << endl;
			average_blocks[i] += my_vector[i*new_size+j];
		}
        //cout << endl;
		average_blocks[i] /= new_size;
		//cout << average_blocks[i] << "	" << average_total <<endl;
	}
	
	double error=0;
	
	// Error calculation
	for(int i = 0; i < NR_BLOCKS; i++)
		error += (average_blocks[i]-average_total)*(average_blocks[i]-average_total);
	
	error = sqrt(error/(NR_BLOCKS-1));
	
	return error;
}
