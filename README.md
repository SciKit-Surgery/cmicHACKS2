# Slides :nut_and_bolt: Hacking Real-time AI workflows for Surgery :wrench: 

## 💻 Machine and OS
```
$ hostnamectl

 Static hostname: --
       Icon name: computer-laptop
         Chassis: laptop
      Machine ID: --
         Boot ID: --
Operating System: Ubuntu 22.04.1 LTS              
          Kernel: Linux 5.15.0-56-generic
    Architecture: x86-64
 Hardware Vendor: --

```

## 💾 Requirements and dependencies for GNU/Linux
```
sudo apt-get install ruby-full build-essential zlib1g-dev
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
gem install jekyll bundler
```
For others OSs, see https://jekyllrb.com/docs/installation/


## 💻 Local testing of html slides

Open two terminals: 
1. to build the site:     
```
bundle exec jekyll serve
```
2. Open hmtl slides using firefox on a local server.
```
firefox http://127.0.0.1:4000 #or google-chrome http://127.0.0.1:4000
firefox http://127.0.0.1:4000/pre-workshop-slides/
firefox http://127.0.0.1:4000/work-achieved/
```
3. You might like to remove build files
```
rm -rf .jekyll-cache/ _site/ Gemfile.lock
```

## 🎒 Steps to create github pages 
1. Setting up pages at https://github.com/SciKit-Surgery/cmicHACKS2/settings/pages
2. Select deploy from a branch, select branch `gh-pages` with path `/root` and[SAVE]. Then, you might need to select `main` branch for the final version of the slides.
3. First GitHub action:  https://github.com/SciKit-Surgery/cmicHACKS2/actions/runs/6747753816
4. Online slides should be available here https://scikit-surgery.github.io/cmicHACKS2


## References 
* https://github.com/oss-for-surgtech/ucl-open-science-awards-2023/tree/main/slides 
* https://github.com/mxochicale/tools/tree/main/html-slides  
* ONLINE-HTML-SLIDES: https://mxochicale.github.io/tools/html-slides/template/slides.html  
* HMTL-SOURCE: https://github.com/mxochicale/tools/blob/main/html-slides/template/slides.html  
* https://github.com/hakimel/reveal.js/tree/master/dist/theme 
* https://github.com/mcanouil/awesome-quarto#presentations
