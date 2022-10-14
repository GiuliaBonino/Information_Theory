clc
clear all
close all
mat=[30 0 10;30 0 70;  30 1 20; 30 1 80; 60 0 40; 60 0 60; 60 1 50; 60 1 60]
c=[0 0 0 1 0 1 0 1]
MAX=max(mat(:))
MIN=min(mat(:))


for i=1:1:size(mat,2)
    for j=1:1:size(mat,1)

    end
end

function best_t=threshold(v)
    for i=1:1:size(v)
        calc_igr
    end
function res=calc_igr(v, c, t)
   tot1=sum(v>t)
   tot2=size(v)-tot1
   p_1=0
   
   tot2=size(v)-tot1
   for i=1:1:size(v)
        if v(i)>t && c(i)==1
            p_1=p_1+1
        end
        if v(i)<=t && c(i)==1
            p_2=p_2+1
        end
    end
   p_1=p_1/tot1
   p_1not=1-p_1
   p_2=p_2/tot2
   p_2not=1-p_2
   H_cond=p_1*log2(1/p_1)+p_1not*log2(1/p_1not)
   H_cond2=p_2*log2(1/p_2)+p_2not*log2(1/p_2not)


end


function res=calc_H_C(v)
    p_1=0
    p_2=0
    for i=1:1:size(v)
        if c(i)==0
            p_1=p_1+1
        elseif c(i)==1
            p_2=p_2+1
        end
    end
    p_1=p_1/size(v)
    p_2=p_2/size(v)
res=p_1*log2(1/p_1)+p_2*log2(1/p_2)
end
    
    