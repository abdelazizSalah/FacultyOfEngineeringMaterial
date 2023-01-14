[x1,fs1] = audioread('Adham.m4a');
[x2,fs2] = audioread('abdelaziz.m4a');
[x3,fs3] = audioread('third.m4a');
x1=x1(:,1);
x2=x2(:,1);
x3=x3(:,1);

%==============================Plot The Three Signals=====================================

plot_all(x1,fs1,'x1');
plot_all(x2,fs2,'x2');
plot_all(x3,fs3,'x3');
fs=min([fs1,fs2,fs3]);
max_len=max([length(x1),length(x2),length(x3)]);
t = linspace(0,max_len/fs,max_len);
x1 = [x1; transpose(zeros(1, max_len - length(x1)))];
x2 = [x2; transpose(zeros(1, max_len - length(x2)))];
x3 = [x3; transpose(zeros(1, max_len - length(x3)))];

%==============================Modulation=====================================
carrier_one_freq=8000;
carrier_two_freq=2.5*carrier_one_freq;

carrier1=cos(2*pi*carrier_one_freq*t);
carrier2=cos(2*pi*carrier_two_freq*t);
carrier3=sin(2*pi*carrier_two_freq*t);

s=x1.*carrier1.'+x2.*carrier2.'+x3.*carrier3.';

%Draw The Modulated Audio
figure;
subplot(3,1,1);
plotting(t,s,'Time','Amplitude','The Modulated Audio in Time Domain');

%Calculate Fourier Transform
[m,phase,f]=calc_fft(s,carrier_two_freq);

%Draw The Modulated Audio Amplitude in Freqency Domain
subplot(3,1,2);
plotting(f,m,'Freqency','Amplitude','The Modulated audio in frequency domain(amplitude)');

%Draw The Modulated Audio Phase in Freqency Domain
subplot(3,1,3);
plotting(f,phase,'Freqency','Phase','The Modulated audio in frequency domain(phase)');

%==============================Demodulation 1=====================================
phase_shift=0;
frequency_shift=0;
demodulation_function(carrier_one_freq,carrier_two_freq,s,fs,t,phase_shift,frequency_shift,'demodulated');

%==============================Demodulation 2(with phase shift)=====================================
phase_shift=10;
frequency_shift=0;
title='withPhaseShift10';
demodulation_function(carrier_one_freq,carrier_two_freq,s,fs,t,phase_shift,frequency_shift,title)

phase_shift=30;
frequency_shift=0;
title='withPhaseShift30';
demodulation_function(carrier_one_freq,carrier_two_freq,s,fs,t,phase_shift,frequency_shift,title)

phase_shift=90;
frequency_shift=0;
title='withPhaseShift90';
demodulation_function(carrier_one_freq,carrier_two_freq,s,fs,t,phase_shift,frequency_shift,title)

%==============================Demodulation 3(with frequency shift)=====================================

phase_shift=0;
frequency_shift=2;
title='withFrequencyShift2';
demodulation_function(carrier_one_freq,carrier_two_freq,s,fs,t,phase_shift,frequency_shift,title)

phase_shift=0;
frequency_shift=10;
title='withFrequencyShift10';
demodulation_function(carrier_one_freq,carrier_two_freq,s,fs,t,phase_shift,frequency_shift,title)


function [m,phase,f] = calc_fft(x,fs)
    N=length(x);
    ftx=fft(x);
    m=abs(fftshift(ftx));
    phase=unwrap(angle(ftx));
    f=(0:N-1)*fs/N;
    f=f-fs*(N-1)/(2*N);
end

function plotting(x,y,labelx,labely,ptitle)
    plot(x,y);
    title(ptitle);
    ylabel(labely);
    xlabel(labelx);
end

function plot_all(y,fs,title)
% Set The Time Vector
t = linspace(0,length(y)/fs,length(y));

figure();
% Draw The Audio in Time Domain
subplot(3,1,1);
plotting(t,y,'Time','Amplitude',strcat('The audio in time domain (',title,')'));

% Calculate Fourier Transform
[m,phase,f]=calc_fft(y,fs);

% Draw The Audio Amplitude in Freqency Domain
subplot(3,1,2);
plotting(f,m,'Freqency','Amplitude',strcat('The audio in frequency domain(amplitude) (',title,')'));


% Draw The Audio Phase in Freqency Domain
subplot(3,1,3);
plotting(f,phase,'Freqency','Phase',strcat('The audio in frequency domain(phase) (',title,')'));
end

function plot_demodulated(demodulated,fc,t,title)
    % Draw The Demodulated Audio
figure;
subplot(3,1,1);
plotting(t,demodulated,'Time','Amplitude',strcat('Demodulated Audio in Time Domain (',title,')'));

% Calculate Fourier Transform
[m,phase,f]=calc_fft(demodulated,fc);

% Draw The Demodulated Audio Amplitude in Freqency Domain
subplot(3,1,2);
plotting(f,m,'Freqency','Amplitude',strcat('The Demodulated audio in frequency domain(amplitude) (',title,')'));

% Draw The Demodulated Audio Phase in Freqency Domain
subplot(3,1,3);
plotting(f,phase,'Freqency','Phase',strcat('The Demodulated audio in frequency domain(phase) (',title,')'));
end



function demodulation_function(carrier_one_freq,carrier_two_freq,s,fs,t,phase_shift,frequency_shift,title)
d_carrier1=cos(2*pi*(carrier_one_freq+frequency_shift)*t+phase_shift/180*pi);
d_carrier2=cos(2*pi*(carrier_two_freq+frequency_shift)*t+phase_shift/180*pi);
d_carrier3=sin(2*pi*(carrier_two_freq+frequency_shift)*t+phase_shift/180*pi);

demodulated_x1=s.*d_carrier1.';
demodulated_x1=2*demodulated_x1;
demodulated_x1=lowpass(demodulated_x1,2000,fs,'Steepness',0.95);
audiowrite(strcat(title,'x1.wav'),demodulated_x1,fs);

demodulated_x2=s.*d_carrier2.';
demodulated_x2=2*demodulated_x2;
demodulated_x2=lowpass(demodulated_x2,2000,fs,'Steepness',0.95);
audiowrite(strcat(title,'x2.wav'),demodulated_x2,fs);

demodulated_x3=s.*d_carrier3.';
demodulated_x3=2*demodulated_x3;
demodulated_x3=lowpass(demodulated_x3,2000,fs,'Steepness',0.95);
audiowrite(strcat(title,'x3.wav'),demodulated_x3,fs);



plot_demodulated(demodulated_x1,carrier_two_freq,t,title);
plot_demodulated(demodulated_x2,carrier_two_freq,t,title);
plot_demodulated(demodulated_x3,carrier_two_freq,t,title);
end