clc;
close all;
clear all;



[xt, fs] = audioread('audio.mp3');


%-------- Time domain ---------- 
t = linspace(0, length(xt)/fs , length(xt));
f = -fs/2 : fs/length(t) : fs/2 - fs/length(t);
figure;
plot(t, xt);
title ('time domain');
xlabel('time');
ylabel('amplitude');


%-------- Freq domain ------------
mf = fftshift(fft(xt));
figure;
plot(f, abs(mf));
title ('freq domain');
xlabel('freq');
ylabel('amplitude');


figure;
plot(f, unwrap(angle(mf)));
title ('freq domain');
xlabel('freq');
ylabel('phase');



%----------- Carrier modulation ------------
ct = cos(2*pi*7600*t);
cf = abs(fftshift(fft(ct)))/fs;

% modulation index ---------> Ac = Mp/mui
mui = 0.8;
Ac = abs(min(xt))/mui;
st = (xt + Ac).*ct';

figure;
plot(t,st);
title ('After Modulation');
xlabel('time');
ylabel('amplitude');


sf = fftshift(fft(st));
figure;
plot(f, abs(sf));
title ('modulation freq domain');
xlabel('freq');
ylabel('amplitude');

figure;
plot(f, unwrap(angle(sf)));
title ('modulation freq domain');
xlabel('freq');
ylabel('phase');

%------------ Demodulation ---------------
recv_signal = st.*ct';
recv_signal_after_lpf = lowpass(recv_signal,7600, fs, 'Steepness', 0.95);

recv_signal_after_lpf = recv_signal_after_lpf - 0.5*Ac;
sound (recv_signal_after_lpf, fs);

figure;
plot(t,recv_signal_after_lpf);
title ('After deModulation');
xlabel('time');
ylabel('amplitude');


recv_signal_after_lpf_freq = fftshift(fft(recv_signal_after_lpf));
figure;
plot(f, abs(recv_signal_after_lpf_freq));
title ('demodulation freq domain');
xlabel('freq');
ylabel('amplitude');


figure;
plot(f, unwrap(angle(recv_signal_after_lpf_freq)));
title ('demodulation freq domain');
xlabel('freq');
ylabel('phase');