require(graphics); require(grDevices)
library(plotly)

# x  <- as.matrix(mtcars)
data <- matrix(c(4030,336,199,167,636,208,151,71,481,221,295,215,378,165,352,740),
            nrow=4,
            ncol=4,
            byrow = TRUE)

dimnames(data) = list(c("Very Low", "Low", "Medium", "High"), c("Very Low", "Low", "Medium", "High"))
#basic heatmap
plot_ly(x=colnames(data), y=rownames(data), z = data, type = "heatmap")

# with normalization (right)
# data=apply(data, 2, function(x){x/mean(x)})
# plot_ly(x=colnames(data), y=rownames(data), z = data, type = "heatmap")

f <- list(
  family = "Courier New, monospace",
  size = 18,
  color = "#000000"
)

x <- list(
  title = "x Axis",
  titlefont = f
)
y <- list(
  title = paste0(c(rep("&nbsp;", 10),
                   "y Axis",
                   rep("&nbsp;", 10),
                   rep("\n&nbsp;", 5)),
                 collapse = ""),
  titlefont = f
)
m <- list(l=100, r=20, b=70, t=10)
plot_ly(x=colnames(data), y=rownames(data), z = data, type = "heatmap", colors = colorRamp(c("yellow", "red"))) %>%
  layout(margin = m, xaxis = x, yaxis = y)
