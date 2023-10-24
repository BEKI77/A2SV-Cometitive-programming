class NumMatrix {
    vector<vector<long>> prefixsum;
public:
    NumMatrix(vector<vector<int>>& M) {
        int row = M.size() + 1, col = M[0].size() + 1;
        prefixsum = vector<vector<long>>(row, vector<long>(col, 0));
        for (int i = 1; i < row; i++)
            for (int j = 1; j < col; j++)
                prefixsum[i][j] = M[i-1][j-1] + prefixsum[i-1][j] + prefixsum[i][j-1] - prefixsum[i-1][j-1];
    }
    
    int sumRegion(int R1, int C1, int R2, int C2) {
        return (int)(prefixsum[R2+1][C2+1] - prefixsum[R2+1][C1] - prefixsum[R1][C2+1] + prefixsum[R1][C1]);
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */