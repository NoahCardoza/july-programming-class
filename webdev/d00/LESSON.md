## What is HTML?
HTML is the standard markup language for creating Web pages. HTML is the markup language that we use to structure and give meaning to our web content, for example defining paragraphs, headings, and data tables, or embedding images and videos in the page. HTML is like the skeleton of the page.

+ HTML stands for Hyper Text Markup Language
+ HTML describes the structure of Web pages using markup
+ HTML elements are the building blocks of HTML pages
+ HTML elements are represented by tags
+ HTML tags label pieces of content such as "heading", "paragraph", "table", and so on
+ Browsers do not display the HTML tags, but use them to render the content of the page

## What is CSS?
CSS is a language of style rules that we use to apply styling to our HTML content, for example setting background colors and fonts, and laying out our content in multiple columns. CSS can be thought of as the skin and page.

+ CSS stands for Cascading Style Sheets
+ CSS describes how HTML elements are to be displayed on screen, paper, or in other media
+ CSS saves a lot of work. It can control the layout of multiple web pages all at once
+ External stylesheets are stored in CSS files

## What is JavaScript?

JavaScript is the programming language of the Web. It is a scripting language that enables you to create dynamically updating content, control multimedia, animate images, and pretty much everything else. (Okay, not everything, but it is amazing what you can achieve with a few lines of JavaScript code.)

---

## HTML Tags:
HTML tags are formatted like so: `<name attribute="value"></name>`
Here are some of the most common tags:

| Tag      | Definition                                                                                                                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `html`   | This wraps the whole document.                                                                                                                         |
| `head`   | This is where **CSS** and some **JS** is loaded.                                                                                                       |
| `title`  | This is where the title in the browser window is set.                                                                                                  |
| `style`  | You can add CSS into this tag.                                                                                                                         |
| `body`   | This is where all of your content should stay.                                                                                                         |
| `span`   | This is an inline element which is used mostly to wrap/section off text.                                                                               |
| `div`    | This is a block element. The `div` tag is probably the most used tag. It is used for everything from content separation to creating art and much more. |
| `a`      | This lets you create hyperlinks which lets you send your users to other pages.                                                                         |
| `h[1-6]` | The 'h' stands for 'heading' basically just big text used for titles. The numbers range from 1 to 6. 1 being the biggest and 6 the smallest.           |
| `img`    | This tag lets you add images to your web site.                                                                                                         |
| `button` | This tag creates a clickable button if you didn't are ready guess!                                                                                     |
| `ul`     | Stands for 'unordered list.'                                                                                                                           |
| `ol`     | Stands for 'ordered list.'                                                                                                                             |
| `li`     | Stands for 'list item.'                                                                                                                                |

This is the basic structure of any html page.

```html
<!DOCTYPE html>
<html>
  <head>
    <title></title>
  </head>
  <body>

  </body>
</html>
```

---

## CSS Rules
Here is how CSS rules are formatted:

![CSS Format](https://www.w3schools.com/css/selector.gif)

There are way to many CSS rules to cover in depth. Here are a few of the one's we will be using:
```CSS
selector {
  /* comment */
  color: white;
  background-color: black;
  width: 50%;
  height: 500px;
  border: 3px #F9CE35 solid;
  text-align: center;
}
```
