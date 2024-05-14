library(data.table)

tweets = fread("./data/export-data-io/from-reda_getachew-tweets-2023-04-26-part1.csv")

# cleaning ----
selected_vars = c(
  "Tweet Posted Time", "Tweet Text", "Tweet Text Length", "Client", "Total Views",
  "Total Retweets", "Total Likes", "Total Quoted", "Total Replies", "Total Bookmarks",
  "Language", "Replying To Username", "Mentions", "Hashtags"
)

tweets = tweets[, ..selected_vars]

setnames(tweets, \(x) tolower(x) |> gsub("[ [:punct:]]+", "_", x = _))

# analysis ----

# hashtag counts
hashtags = tweets[, unlist(strsplit(hashtags, ","))] |>
  table() |>
  as.data.table() |>
  setNames(c("hashtag", "count"))

hashtags = hashtags[order(-count), ]
