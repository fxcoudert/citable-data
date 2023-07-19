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
    int number_file = 1; 
    
	vector<string> files(number_file,"");
	
	stringstream ss;
	
	// declare file
	for(int i=1; i<=number_file; i++)
	{
		ss << i;
		files[i-1] = "NCMC_chemical_potential_alchemical_transformation/AlchemicalWork.txt";
		ss.str("");
	}
	
	ifstream iFS;
	
	vector<int> lines(number_file,0);
	
	string buffer;
	
	// Load the trajectory and count lines	
	for(int i = 0; i < number_file; i++)
	{
		iFS.open(files[i].c_str());
		if(iFS)
		{
			while(getline(iFS, buffer))
			{
				lines[i]++;
			}
		}
		else
		{
			cout << "Cannot open file " << files[i] << endl;
		}
		
		lines[i]--; // remove the first line (which is text).
	
		iFS.close();
		iFS.clear();
	}
	
	double number_1;
	double number_2;
	double number_3;
	
	vector<double> W;
	
	// Store quantity
	for(int i = 0; i < number_file; i++)
	{
		iFS.open(files[i].c_str());
		if(iFS)
		{
			getline(iFS, buffer);
			for(int j = 0; j < lines[i]; j++)
			{
				iFS >> number_1 >> number_2 >> number_3;
				W.push_back(number_3);
			}
		}
		else
		{
			cout << "Cannot open file " << files[i] << endl;;
		}
	
		iFS.close();
		iFS.clear();
	}
	
	//---------------------------------//
		// Compute of protocol work
	//---------------------------------//
	
	W.resize(3001);
	
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
	
	average_mu = -KT*log(139*140/(6*6)*average_exp_W);
	error_mu = KT*error_exp_W/average_exp_W;
    

	// Output file.

	string output = "Results_osmostat_CsCl_6_pairs.txt";

	ofstream oFS;
	
	oFS.open(output.c_str());
	
	if(oFS)
	{
		oFS << "osmostat: 2*H20 -> CsCl: Number of pseudo widom attemps: \t";
		oFS << W.size();
		oFS << ". " << endl;
		oFS << "Average Protocol Work :\t\t\t\t\t\t\t" << average_W << " +/- " << error_W << " kJ/mol." << endl;
		oFS << "Chemical potential :\t\t\t\t\t\t\t" << average_mu << " +/- " << error_mu << " kJ/mol." << endl;
	}
	else
	{
		cout << "Cannot open file." << endl;
	}
	
	oFS.close();
	oFS.clear();

    output = "protocol_work_CsCl_6_pairs.txt";

    oFS.open(output.c_str());

    if(oFS)
    {
        oFS << "Protocol Work (kJ/mol)" << endl;
        for(int i = 0; i < W.size(); i++)
            oFS << i << " " << W[i] << endl;
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
