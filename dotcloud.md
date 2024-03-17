---
title: "Dotcloud Made My Life Easier"
date: 2012-05-09
---
<div id="alert_info" class="flex p-4 mb-4 text-gray-600 dark:text-gray-500 bg-yellow-100 dark:bg-slate-900 rounded-lg" role="alert">

  <svg aria-hidden="true" class="flex-shrink-0 w-5 h-5 mt-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path></svg>

  <div class="ml-3 text-base">
    Please note that this post is more than <strong>10 years old</strong>. dotCloud was a groundbreaking PaaS company that developed a container engine which later became the widely popular <strong>Docker</strong> platform. Docker has since revolutionized the way we develop, deploy, and manage applications, making it an essential tool for many developers and organizations today.
  </div>
</div>

[dotCloud](https://web.archive.org/web/20110728103356/https://www.dotcloud.com/) is one of my favourite companies. They're a platform-as-a-service (PaaS) start-up supporting variety of stacks such as Java, Ruby, PHP, Python, Perl and node.js.

As much as I enjoy working with unix systems and setting up web servers, they shift my main focus: developing web applications. As a one man show, my time is very scarce. While I was working with PHP, hosting apps used to be extremely simple. I could easily get a dirt cheap shared hosting for a few bucks and FTP the code. Even for bigger applications, setting up a LAMP stack was and still is very simple. However, PHP days are over and Python/Django is what I use for most of the web development.

I've used two ways to host Django applications. For small apps I've used [Webfaction](http://webfaction.com/) which is also a great company and highly recommended for shared hosting. Sharing servers with others have always been painful for me so the next solution was a virtual server. [Linode](http://linode.com/) is my preferred VPS provider and they've been amazing. This is probably the best bang for your buck.

For a recent project I needed this stack:

*   Django
*   PostgreSQL
*   MongoDB
*   Solr

To setup all these manually in your VPS, you'll need multiple servers, good technical knowledge, lots of time and patience. Setting up these might take a day or two, but securing, maintaining and scaling them would take a lot longer.

This is where dotCloud shines. I can easily deploy multiple stacks which are secure, have redundancy, and can scale with a few commands. Deploying staging/development servers would also take a few seconds (try this with your VPS). With their new pricing model, you can have unlimited development apps which is great for people like me who start many projects and complete a few ! :)

What I don't like about dotCloud:

*   No servers in Europe.
*   According to their new beta pricing, databases are billed by their RAM usage. I think this should be based on storage.
*   No naked domains. You have to use www before your domain name, which is a big limitation.
*   Support. With [10M investment](http://gigaom.com/cloud/dotcloud-gets-10m-to-redefine-cloud-openness/), you would think they could hire a few people to work in the weekends. But no, my app was down for 12 hrs in one weekend, and the reply I got was "On week-ends, our on-call team get paged only by Enterprise Plan customers." I wasn't in the position to complain as a non-paying beta user, but it still was disappointing.

I want to thank dotCloud for making my life much easier and less stressful. [Ep.io](https://www.ep.io/blog/epio-closing-down/) and [Djangy](http://news.ycombinator.com/item?id=2269406) are two Django specific PaaS's who couldn't stay around. I'm hopeful that dotCloud will make it.
