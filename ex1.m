
x=0
y=0
z=0
n=1
for i=0.001:0.001:1
   for j=0.001:0.001:1
      if i+j<1
          k=1-i-j;
          x(n)=i;
          y(n)=j;
          z(n)=k;
          n=n+1;
      end
    end
end

H=0


 H=x.*log2(1./x)+y.*log2(1./y)+z.*log2(1./z);
max=0
index=0
 for i=1:size(H,2)
    if H(i)>max
        
        max=H(i);
        index=i;
    end
 end

 figure(1)
 colormap jet
 sphere=30
 scatter(x,y,sphere, H), hold on
%plot(x(index), y(index), 'bo', 'MarkerSize',8, 'MarkerFaceColor','w')
 colorbar
 xticks([0:0.1:1])
 yticks([0:0.1:1])

 xlabel("p_1")
 ylabel("p_2")
 grid on
 p_1=0.54
 p_2=0.15
 plot(p_1, p_2, 'bo', 'MarkerSize',8, 'MarkerFaceColor','b')
 avg=(p_1+p_2)/2
 plot(avg, avg, 'bo', 'MarkerSize',8, 'MarkerFaceColor','g')
tit=sprintf('H_{MAX}=%.2f p_1=%.2f p_2=%.2f p_3=%.2f ', max, x(index), y(index), z(index))
title(tit)







