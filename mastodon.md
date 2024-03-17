---
title: "Single-user Mastodon Instance is a Bad Idea"
description: "If you're thinking about setting up your own single-user Mastodon instance, I urge you not to do it. The user experience is so broken that it's baffling that anyone would find it acceptable."
date: 2023-03-10
image_url: https://static.mull.net/mastodon/mastodon.jpg
mastodon: https://mas.to/@mull/110002247016793805
---
![A portrait of a Mastodon](https://static.mull.net/mastodon/mastodon.jpg "DALL-E prompt: A 3D render of a mastodon walking in a green desert")

Mastodon takes me back to the early days of the internet, before algorithms, advertising, and dopamine-driven feedback loops tainted the user experience. While Mastodon hasn't quite reached mainstream status, the existing communities are enjoyable and breath of fresh air compared to what Twitter has become.

I've had an account on the largest Mastodon instance since 2016, but I wanted to host my own Mastodon instance so that I could take ownership of my data, control my online presence, and own my handle that I can keep forever. In the past, I migrated my account to different hosts multiple times; however, due to the semi-broken portability of accounts (i.e., the inability to move posts and lists), I decided to have my own instance.

If you're thinking about setting up your own single-user Mastodon instance for similar reasons, I urge you **not to do it**. The user experience is so broken that it's baffling that anyone would find it acceptable.

Since the Mastodon application is like the mammal it's named after (big and slow), I had no intention of maintaining a server. Instead, I used the awesome managed Mastodon host [masto.host](https://masto.host/). The setup was easy and quick, and my instance was up in less than an hour.

However, I wasn't prepared for what came next, mostly because I didn't fully understand how the fediverse works. I should have done my research earlier.

As the only user on my instance, the content I received via federation was extremely limited, which broke the user experience. Here are the major issues I faced:

- **Missing posts on user profiles**: If you visit a profile of someone you don't follow, you won't see their posts except the pinned ones.

- **Missing replies on posts**: Mastodon doesn't ensure it gets all replies to remote posts. As the replies aren't sent to non-followers, your instance won't be aware of them. This was a dealbreaker for me since I could only see a fraction of the replies to the posts on my timeline, and I couldn't get the full context of the conversation.

- **Post stats are either empty or inaccurate**: For the same reason as above, boosts and favorite counts are also missing.

- **Explore/Trending timeline doesn't exist**: Since my instance received very few posts, it couldn't generate a trending timeline, making this feature useless. The local timeline was also pointless since it was just me.

- **Cannot follow hashtags**: While technically possible, it's useless since you won't discover any meaningful volume of posts. This was one of my favorite features on the larger instance as I follow many less-popular hashtags to discover content and connect with like-minded people. This was another dealbreaker for me.


- **Your discoverability is broken**: Hashtags are a great way to discover content/people and be discovered. But almost no one outside of your followers will see your hashtagged posts. If you have a large follower list, this might not be a huge issue as your content would be discovered by other instances.

Some of these issues can be improved by using relays, but I don't find it to be a feasible solution. It's hard to find relays that will accept you as a single-user instance, and it's too taxing for your server, with exponentially more processing, space, and memory requirements.

I do understand the technical reasons behind most of those issues. Some of them should be easier to solve. For example, why doesn't the server fetch the X number of recent posts of a profile that I visit? Despite the open Github issues ([1](https://github.com/mastodon/mastodon/issues/34), [2](https://github.com/mastodon/mastodon/issues/14017), [3](https://github.com/mastodon/mastodon/discussions/22608)), it doesn't seem like there's a plan or desire to address them. Fortunately, apps like Mammoth and Mona are attempting to handle these issues gracefully on the client side, but my favorite app Ivory doesn't yet.

At the end, while I loved using my own domain as my handle and owning my data, the user experience immediately became less enjoyable. I migrated back to [mastodon.social](https://mastodon.social/@erinc), the original and the largest instance. [Follow me](https://mastodon.social/@erinc) there.