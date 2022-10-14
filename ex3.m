mat=[0.37 0.17; 0.14 0.02; 0.24 0.05]

p_x=[0.37+0.17; 0.14+0.02; 0.24+0.05]
p_y=[0.37+0.14+0.24; 0.17+0.02+0.05]


H_x=0
for i=1:size(p_x,1)
    H_x=H_x+p_x(i)*log2(1/p_x(i))
end
H_y=0
for i=1:size(p_y,1)
    H_y=H_y+p_y(i)*log2(1/p_y(i))
end

px_cond_y=0
n=1
for i=1:size(mat,1)
    for j=1:size(mat,2)
        px_cond_y(n)=mat(i,j)/p_x(i)
        n=n+1
    end
end

py_cond_x=0
m=1
for i=1:size(mat,1)
    for j=1:size(mat,2)
        py_cond_x(m)=mat(i,j)/p_y(j)
        m=m+1
    end
end

Hx_cond_y=0

for i=1:size(mat,1)
    for j=1:size(mat,2)
        Hx_cond_y= Hx_cond_y+ mat(i,j)*log2(p_y(j)/(mat(i,j)));
    end
end

Hy_cond_x=0

for i=1:size(mat,1)
    for j=1:size(mat,2)
        Hy_cond_x= Hy_cond_x+ mat(i,j)*log2(p_x(i)/(mat(i,j)));
    end
end






