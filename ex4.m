    num=[1 3 2 8 22 45 44 42 24 8 3]
x_i=[0 1 2 3 4 5 6 7 8 9 10]

p_i=num/sum(num)
N=11
q_i=zeros(N, 1)
q_i(:)=1/N


for p=0.001:0.001:1
    bin_i=binopdf(x_i, 11, p)
    d=KL(x_i, p_i, bin_i)
    if p==0.001
        min=d
        p_min=p
    end

    if d<min
        min=d
        p_min=p
    end
end

figure
y=binopdf(x_i, 11,p_min)
bar(x_i,y, 1)
xlabel('Observation')
ylabel('Probability')


function f=KL(x, p, q)
    dist=0
  for i=1:size(x,2)
    dist=dist+p(i)*log2(p(i)/q(i))
  end  
  f=dist
end

